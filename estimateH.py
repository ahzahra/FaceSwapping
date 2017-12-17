import cv2 
import numpy as np

def getAffineTransform(src_pts, dst_pts):
    """
    Return an affine transformation [s * R | T] such that:
        sum ||s*R*p1,i + T - p2,i||^2
    is minimized.
    """
    # Solve the procrustes problem by subtracting centroids, scaling by the
    # standard deviation, and then using the SVD to calculate the rotation. See
    # the following for more details:
    #   https://en.wikipedia.org/wiki/Orthogonal_Procrustes_problem

    src_pts = src_pts.astype(numpy.float64)
    dst_pts = dst_pts.astype(numpy.float64)

    c1 = numpy.mean(src_pts, axis=0)
    c2 = numpy.mean(dst_pts, axis=0)
    src_pts -= c1
    dst_pts -= c2

    s1 = numpy.std(src_pts)
    s2 = numpy.std(dst_pts)
    src_pts /= s1
    dst_pts /= s2

    U, S, Vt = numpy.linalg.svd(src_pts.T * dst_pts)

    # The R we seek is in fact the transpose of the one given by U * Vt. This
    # is because the above formulation assumes the matrix goes on the right
    # (with row vectors) where as our solution requires the matrix to be on the
    # left (with column vectors).
    R = (U * Vt).T

    return numpy.vstack([numpy.hstack(((s2 / s1) * R,
                                       c2.T - (s2 / s1) * R * c1.T)),
                         numpy.matrix([0., 0., 1.])])