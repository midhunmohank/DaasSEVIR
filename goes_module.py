import boto3

def day_of_year(year, month, day):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        days_in_month[2] = 29
        
    day_of_year = sum(days_in_month[:month]) + day
    return day_of_year

def get_files_goes(year, month, day, hour):
    day_year = day_of_year(int(year), int(month), int(day))
    print(day_year)

    s3 = boto3.client("s3")
    bucket_name = "noaa-goes18"
    if(year != "2022" and year != "2023"):
        print("Not a Valid Year")
    #    return "Not Valid Year"

    else:
        prefix =  product + "/" + str(year) + "/" + str(day_year) + "/" + str(hour) + "/"
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix = prefix)
        print(response)
        objects = response.get("Contents", []) 
        return [obj["Key"] for obj in objects]
    
def get_url_goes_original(filename):
    split = filename.split('_')
    # Extracting the timestamp
    timeStamp = split[4][1:]
    year = timeStamp[:4]
    day = timeStamp[4:7] 
    hour = timeStamp[7:9]

    #Extracting the Product Name
    productName = split[1]
    productName = productName.rsplit('-',1)[0][:-1]
    s3Bucket = split[2][1:3]
    link = f'https://noaa-goes{s3Bucket}.s3.amazonaws.com/{productName}/{year}/{day}/{hour}/{filename}'
    return link


    
    

   