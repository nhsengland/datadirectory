### NHS England Data Directory

Listings website for the NHS England Health Data Directory.

### Generating the Directory

1. Data is gathered from a survey / research process.

2. Data is exported from the survey to a CSV file.

3. The CSV data is transformed to our Data Directory Dataset format

4. The new dataset is uploaded to CKAN, along with annotations for datasets

5. The new Directory website is generated from the dataset

6. The new Directory website is deployed

7. There is no step 7.

### 3. Transforming data

Data transformations are performed using the Rakefile in this repository. They
expect the survey output to be named "dataset.csv".

    rake transform

### 5. Generating the Directory website

Generating a Directory website from the data is done by the Rakefile in this
repository. The script expects the dataset to be available in the file "data.directory.csv".

    rake generate
    rake commit