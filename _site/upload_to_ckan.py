"""
Script to upload the dataset to CKAN.
"""
import datetime
import ckanapi

CKAN = 'http://ec2-52-50-169-162.eu-west-1.compute.amazonaws.com'
APIKEY = '18a5e9d1-1c4a-422f-bfd6-53945ff99cf1'

catalogue = ckanapi.RemoteCKAN(CKAN, apikey=APIKEY)
today = datetime.date.today().strftime('%Y/%m/%d')

try:
    pkg = catalogue.action.package_show(id='datadirectory')
except ckanapi.errors.NotFound:
    pkg = catalogue.action.package_create(owner_org='nhs-england',
                                          name="datadirectory",
                                          title='NHS England Data Directory')
pkg['license_id'] = 'ogl'
catalogue.action.package_update(**pkg)

catalogue.action.resource_create(**
    {
        'package_id' : 'datadirectory',
        'description': 'Source data for the Health Data Directory release {0}'.format(today),
        'format'     : 'csv',
        'upload'     : open('data.directory.csv')
    })
