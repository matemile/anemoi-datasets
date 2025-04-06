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
from typing import Any, Dict, Tuple

import earthkit.data as ekd
from anemoi.transform.fields import new_field_from_numpy
from anemoi.transform.fields import new_fieldlist_from_list

from .legacy import legacy_filter

@legacy_filter(__file__)
def execute(context: Any, input: ekd.FieldList, raw: str, mask: str, pp: str = "pp") -> ekd.FieldList:
    """Convert raw Nordic RADAR data which includes NaNs
    to pre-processed RADAR data with zeros

    Parameters
    ----------
    context : Any
        The context in which the function is executed.
    input : FieldList
        List of input fields.
    raw : str
        Raw RADAR data.
    mask : str
        No data mask.
    pp : str
        RADAR data after NaNs are replaced with 
        zeros. Defaults to "pp".

    Returns
    -------
    FieldList
        List of fields with filtered RADAR data.
    """

    result = []
    params: Tuple[str, str] = (raw, mask)
    pairs: Dict[Tuple[Any, ...], Dict[str, Any]] = defaultdict(dict)

    for f in input:
        key = f.metadata(namespace="")
        
        param = key.pop("param")
        
        if param in params:
            key = tuple(key.items())
        
            if param in pairs[key]:
                raise ValueError(f"Duplicate field {param} for {key}")
            
            pairs[key][param] = f
        else:
            result.append(f)

    for keys, values in pairs.items():
        #some checks
        #if len(values) !=2: # it's not the case here...
        #    raise ValueError("Missing fields")
        if ('variable', raw) in keys:
            raw_pl = values[raw].to_numpy(flatten=True)

            f_nans = np.isnan(raw_pl)
            
        if ('variable', mask) in keys:
            mask_pl = values[mask].to_numpy(flatten=True)
        
            #Filtering the output
            output = np.where(f_nans & (mask_pl == 0), 0, raw_pl)

            result.append(new_field_from_numpy(output, template=values[mask], param=pp))

    return new_fieldlist_from_list(result)
