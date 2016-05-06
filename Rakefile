# Rakefile for generating the directory

require 'csv'
require 'erb'

sample_project =   <<-eos
---
layout: nhse_post
title: "<%= @name %>"
author: <%= @orgname %>
orgdescription: "<%= @orgdescription %>"
impact: "<%= @impact %>"
datasets: "<%= @datasets %>"
date: <%= @datestring %>
description: "<%= @usage[0..500] %>"
imageurl: <%= @imageurl %>
external_link: <%= @url %>
order: <%= @order %>
tags:
<% @tags.each do | tag | %>
  - <%= tag %>
<% end %>
---
eos


def putty what
  puts "*" * 80
  puts what
  puts "*" * 80
end

class Project

  def initialize(name, url, usage, impact, orgname, orgdescription, datasets, imageurl, tags, order)
    @name           = name
    @url            = url
    @usage          = usage
    @impact         = impact
    @orgname        = orgname
    @orgdescription = orgdescription
    @datasets       = datasets
    @date           = Time.now
    @datestring     = @date.strftime("%d-%m-%Y %H:%M +0000")
    @imageurl       = imageurl
    @tags           = tags.split ','
    @order          = order
  end

  def slug
    @date.strftime("%d-%m-%y-")+ @name.downcase.strip.gsub(' ', '-').gsub(/[^\w-]/, '')
  end

  def get_binding
    binding()
  end

end

task :transform do
  putty "Transforming the Survey output"
  sh "rm -f data.directory.csv"
  CSV.open('data.directory.csv', 'w') do |dataset|
    dataset << [
      'name', 'url', 'usage',
      'impact',
      'orgname', 'orgdescription',
      'datasets', 'imageurl', 'tags',
      'order'
    ]
    CSV.foreach('exported.data.csv', :headers => true) do |row|
      rowhash = row.to_hash
      if rowhash["Include"] != "Yes"
        next
      end
      putty rowhash["What is the name of your project?"]
      dataset << [
        rowhash["What is the name of your project?"],
        rowhash["Does your project have a website?"],
        rowhash["How did you use open health data?"],
        rowhash["What was the impact of your project?"],
        rowhash["What is the name of your organization?"],
        rowhash["What does your organization do?"],
        rowhash["Datasets"],
        rowhash["Is there an image that represents your project?"],
        rowhash["Tags"],
        rowhash["Order"]
      ]
    end
  end
  putty "New dataset generated at data.directory.csv"
end

task :generate do
  putty "Generating the Directory website"
  sh "rm -f _posts/*"
  template = ERB.new sample_project, nil, "%"

  CSV.foreach('data.directory.csv', :headers => true) do |row|
    rowhash = row.to_hash

    project  = Project.new(
      rowhash['name'], rowhash['url'],
      rowhash['usage'], rowhash['impact'],
      rowhash['orgname'],
      rowhash['orgdescription'],
      rowhash['datasets'], rowhash['imageurl'], rowhash['tags'],
      rowhash['order']
    )

    puts project.slug
    File.write "_posts/#{project.slug}.md", template.result( project.get_binding )
  end
  putty "New Directory website generated"
end

task :commit do
  putty "Making changes permanent"
  sh "git add ."
  now = Time.now.strftime("%d-%m-%Y %H:%M +0000")
  sh "git commit -a -m 'Auto commit from Rakefile #{now}'"
  sh "git push origin gh-pages"
end
