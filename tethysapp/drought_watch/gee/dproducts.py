EE_PRODUCTS = {
    'precip':{
        'chirps': {
                'display': 'Precipitation (CHIRPS)',
                'collection': 'UCSB-CHG/CHIRPS/DAILY',
                'index': 'precipitation',
                'vis_params': {
                    'min': 1.0,
                    'max': 17.0,
                    'palette': ['001137', '0aab1e', 'e7eb05', 'ff4a2d', 'e90000'],

                },
                'start_date': '1981-01-01',
                'end_date': '2022-03-31'  # to present
            }

    },
    'vegetation':{
        'fapar': {
                'display': 'LAI FAPAR',
                'collection': 'NOAA/CDR/AVHRR/LAI_FAPAR/V5',
                'index': 'LAI',
                'vis_params': {
                    'min': 0.0,
                    'max': 4000.0,
                    'palette': ['3b0200', '977705', 'ca9f06', 'ffca09', '006a03', '003b02'],
                },
                'start_date': '1981-06-24',
                'end_date': '2022-05-01'  # to present
            }
    },
    'soilmoisture':{
        'smap': {
                'display': 'SMAP Global Soil Moisture',
                'collection': 'NASA_USDA/HSL/SMAP10KM_soil_moisture',
                'index': 'ssm',
                'vis_params': {
                    'min': 0.0,
                    'max': 28.0,
                    'palette': ['0300ff', '418504', 'efff07', 'efff07', 'ff0303'],
                },
                'start_date': '2015-04-02',
                'end_date': '2022-05-01'  # to present
            }

    }

}
