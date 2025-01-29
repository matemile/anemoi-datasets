###########
 revert_mask
###########

The ``revert_mask`` filter converts is_nodata to a RADAR
mask using the equation:

.. math::

   mask &= (nomask*(-1.0)+1.0) 

This filter needs to transform RADAR mask, which is
a mask of No data.

.. literalinclude:: yaml/revert_mask.yaml
   :language: yaml
