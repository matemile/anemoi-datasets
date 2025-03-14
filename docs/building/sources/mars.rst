######
 mars
######

The ``mars`` source will retrieve the data from the ECMWF MARS archive.
For that, you need to have an ECMWF account and build your dataset on
one of the Centre's computers, or use the ``ecmwfapi`` Python package.

The `yaml` block can contain any keys that following the `MARS language
specification`_, with the exception of the ``date``, ``time``` and
``step``.

The missing keys will be filled with the default values, as defined in
the MARS language specification.

.. literalinclude:: yaml/mars1.yaml
   :language: yaml

Data from several levels types must be requested in separate requests,
with the ``join`` command.

.. literalinclude:: yaml/mars2.yaml
   :language: yaml

See :ref:`naming-variables` for information on how to name the variables
when mixing single level and multi-levels variables in the same dataset.

.. _mars language specification: https://confluence.ecmwf.int/display/UDOC/MARS+user+documentation

*****
 cds
*****

For users outside of ECMWF organisation, it is possible to access ERA5
data through the Copernicus Climate Data Store ``cdsapi`` instead.

The steps to setup a CDS API account are detailed `here
<https://cds.climate.copernicus.eu/how-to-api>`_.

The only difference with the previous MARS recipes is the addition of
the ``use_cdsapi_dataset`` key:

.. literalinclude:: yaml/mars-cds.yaml
   :language: yaml

This process can take some time because of the high demand on the CDS
server.
