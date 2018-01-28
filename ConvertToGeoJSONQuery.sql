select json_build_object(
    'type', 'FeatureCollection',
    'features', jsonb_agg(feature))
from(
    select json_build_object(
        'type',       'Feature',
        'geometry',   ST_AsGeoJSON(geom)::json,
        'properties', json_build_object(
            'UWB', "UWB",
            'BWB', "BWB",
            'AWK', "AWK",
            'BEZ', "BEZ")) as feature
	from (select * from public."BerlinWahlkreise") row) features;