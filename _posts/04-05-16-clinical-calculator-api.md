---
layout: nhse_post
title: clinical calculator API
author: openhealthhub CIC
date: 04-05-2016 14:14 +0000
description: "We created a REST API which conceals some of the complexity of open data, by removing some of the need to understand the document structure, geographical jargon, and clinical meaning of the raw open data, and enabling simple access to  relevant portions of the data.

As an example, the open data on prevalence of obesity is available as a large Excel file from http://www.noo.org.uk/visualisation. It's organised by region, by LSOA, and MSOA, and by electoral ward (geographical jargon). We felt that"
imageurl: 
---
<img src="" />

## <a href="api.clinicalcalculator.org (API only) " target="_blank"> clinical calculator API <i class="fa fa-external-link"></i></a>

We created a REST API which conceals some of the complexity of open data, by removing some of the need to understand the document structure, geographical jargon, and clinical meaning of the raw open data, and enabling simple access to  relevant portions of the data.

As an example, the open data on prevalence of obesity is available as a large Excel file from http://www.noo.org.uk/visualisation. It's organised by region, by LSOA, and MSOA, and by electoral ward (geographical jargon). We felt that many people would want to search by postcode, in order to discover the prevalence of obesity in their area. We therefore used MySociety's MapIt postcode data API https://mapit.mysociety.org/ to return the Ward/MSOA/LSOA for a given postcode, and them used this to look up the relevant information and return it as a JSON response.

To return to what the illustrious David Miller refers to as 'That Old Chestnut' - Clinical Calculator API also provides height centile, weight centile and BMI centile data, used for assessing child growth, general health, and (increasingly) obesity. This is NOT open data, although it definitely should be. In the USA it is open data. http://www.cdc.gov/growthcharts/percentile_data_files.htm

I suggest trying to use the API from Postman with the following example queries:

Centile: GET http://api.clinicalcalculator.org/centile?weight_in_kg=29&height_in_m=1.20&year_of_birth=2006&month_of_birth=11&day_of_birth=10&sex=M

Obesity Data: GET http://api.clinicalcalculator.org/obesity_by_postcode?postcode_search=wn72nx



## Datasets used

we used the Ward and MSOA tables from here: http://www.noo.org.uk/visualisation 

postcodes from here: https://mapit.mysociety.org/

Medical Research Council UK90 LMS Tables (unfortunately this is not open data, I had to apply for a licence to use it from the MRC, which was free, and took a mere 9 months) I had a long discussion with the MRC about making it open data, and their response was [NaN].

## openhealthhub CIC

open health stuff, sort of.