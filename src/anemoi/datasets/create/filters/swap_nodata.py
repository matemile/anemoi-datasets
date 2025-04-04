# (C) Copyright 2024 Anemoi contributors.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.


from collections import defaultdict

from earthkit.data.indexing.fieldlist import FieldArray
from .remove_nans_radar import NewDataField

def execute(context, input, nomask, mask="mask"):
    """Convert nomask [0-1] to mask [1-0]"""
    result = FieldArray()

    processed_fields = defaultdict(dict)

    for f in input:
        output = (f.to_numpy(flatten=True) * (-1.0) + 1.0)
        result.append(NewDataField(f, output, mask))

    return result
