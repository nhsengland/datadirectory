---
layout: nhse_post
title: "clinical calculator API"
author: openhealthhub CIC
orgdescription: "open health stuff, sort of."
impact: ""
datasets: "* [MSOA NCMP child obesity prevalence](http://www.noo.org.uk/visualisation) NCMP obesity prevalence data for Reception (age 4-5 years) and Year 6 (age 10-11 years) children."
date: 09-09-2016 14:17 +0000
description: "We created a REST API which conceals some of the complexity of open data, by removing some of the need to understand the document structure, geographical jargon, and clinical meaning of the raw open data, and enabling simple access to  relevant portions of the data.

As an example, the open data on prevalence of obesity is available as a large Excel file from http://www.noo.org.uk/visualisation. It's organised by region, by LSOA, and MSOA, and by electoral ward (geographical jargon). We felt that many people would want to search by postcode, in order to discover the prevalence of obesity in their area. We therefore used MySociety's MapIt postcode data API https://mapit.mysociety.org/ to return the Ward/MSOA/LSOA for a given postcode, and them used this to look up the relevant information and return it as a JSON response.

Clinical Calculator API also provides height centile, weight centile and BMI centile data, used for assessing child growth, general health, and (increasingly) obesity. This is NOT open data, although it definitely should be. In the USA it is open data. http://www.cdc.gov/growthcharts/percentile_data_files.htm
"
imageurl: http://obesitychallenge.rewiredstate.org/webhook-uploads/1441207772961/cc.jpg
external_link: https://github.com/open-health-hub/clinical_calculator_api
order: 4
tags:

  - api

  - obesity

---
