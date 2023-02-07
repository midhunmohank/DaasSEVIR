
import boto3

#Function to get files given the station, year, month day and hour
def get_files_noaa(station, year, month, day, hour):
    
    s3 = boto3.client("s3")
    bucket_name = "noaa-nexrad-level2"
    if(year != "2022" and year != "2023"):
        print("Not a Valid Year")
        return "Not Valid Year"   
    else:
        prefix = year + "/" + month + "/" + day  + "/" + station
        response = s3.list_objects_v2(Bucket=bucket_name, Prefix = prefix)
        objects = response.get("Contents", []) 
        files = [obj["Key"] for obj in objects]
        files_hour = []
        for i in files: 
            if(i.split("_")[1][:2] == hour):  
                files_hour.append(i) 
        return files_hour
  
#Get the url from noaa website   
def get_url_noaa_original(file_name):
    return "https://noaa-nexrad-level2.s3.amazonaws.com/" + file_name[4:8] + "/" + file_name[8:10] + "/" + file_name[10:12] + "/" + file_name[0:4] + "/" + file_name

    







print(get_files_noaa("KBHX", "2022", "11", "01", "05"))






    
    
    

