---
layout: nhse_post
title: "clinical calculator API"
author: openhealthhub CIC
orgdescription: "open health stuff, sort of."
impact: ""
datasets: "we used the Ward and MSOA tables from here: http://www.noo.org.uk/visualisation 

postcodes from here: https://mapit.mysociety.org/

Medical Research Council UK90 LMS Tables (unfortunately this is not open data, I had to apply for a licence to use it from the MRC, which was free, and took a mere 9 months) I had a long discussion with the MRC about making it open data, and their response was [NaN]."
date: 04-05-2016 16:59 +0000
description: "We created a REST API which conceals some of the complexity of open data, by removing some of the need to understand the document structure, geographical jargon, and clinical meaning of the raw open data, and enabling simple access to  relevant portions of the data.

As an example, the open data on prevalence of obesity is available as a large Excel file from http://www.noo.org.uk/visualisation. It's organised by region, by LSOA, and MSOA, and by electoral ward (geographical jargon). We felt that"
imageurl: http://obesitychallenge.rewiredstate.org/webhook-uploads/1441207772961/cc.jpg
tags:

  - api

  - obesity

---
