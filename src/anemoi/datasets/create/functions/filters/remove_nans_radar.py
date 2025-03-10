# (C) Copyright 2024 Anemoi contributors.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import numpy as np
from collections import defaultdict

from earthkit.data.indexing.fieldlist import FieldArray
from .swap_nodata import NewDataField

def execute(context, input, raw, ppdata="pp"):
    """Convert raw Nordic RADAR data which includes NaNs
    to pre-processed RADAR data with zeros"""
    result = FieldArray()

    processed_fields = defaultdict(dict)

    for f in input:
        f_nans = np.isnan(f)
        f = np.where(f_nans, 0, f)
        output = f.to_numpy(flatten=True)
        result.append(NewDataField(f, output, ppdata))

    return result
