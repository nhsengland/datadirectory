# Rakefile for generating the directory

require 'csv'
require 'erb'

class Project

  def initialize(name, url, usage, orgname, orgdescription, datasets, imageurl)
    @name           = name
    @url            = url
    @usage          = usage
    @orgname        = orgname
    @orgdescription = orgdescription
    @datasets       = datasets
    @date           = Time.now
    @datestring     = @date.strftime("%d-%m-%Y %H:%M +0000")
    @imageurl       = imageurl
  end

  def slug
    @date.strftime("%d-%m-%y-")+ @name.downcase.strip.gsub(' ', '-').gsub(/[^\w-]/, '')
  end

  def get_binding
    binding()
  end

end

task :generate do
  sh "rm -f _posts/*"
  template = ERB.new File.read("sample_project.erb"), nil, "%"

  CSV.foreach('dataset.csv', :headers => true) do |row|
    rowhash = row.to_hash

    project  = Project.new(
      rowhash["What is the name of your project?"], rowhash["Does your project have a website?"],
      rowhash["How did you use open health data?"], rowhash["What is the name of your organization?"],
      rowhash["What does your organization do?"],
      rowhash["What datasets did you use in your project? (Please include links if possible)"],
      rowhash["Is there an image that represents your project?"]
    )

    puts project.slug
    File.write "_posts/#{project.slug}.md", template.result( project.get_binding )

  end
end
