import requests
import json

def construct_api_url(location='', company='', category='', level=''):
    base_url = "https://www.themuse.com/api/public/jobs?"
    params = []

    if location:
        params.append(f"location={location}")

    if company:
        params.append(f"company={company}")

    if category:
        params.append(f"category={category}")

    if level:
        params.append(f"level={level}%20Level")

    params.append("page=1")
    params.append("descending=false")

    return base_url + "&".join(params)

def get_job_data(api_url):
    job_data = requests.get(api_url)
    return job_data.json()

def main():
    company = input("Enter company (leave blank if not specific): ").strip()
    category = input("Enter category (leave blank if not specific): ").strip()
    level = input("Enter level (leave blank if not specific): ").strip()
    location = input("Enter location (city) (leave blank if not specific): ").strip()

    api_url = construct_api_url(location=location, company=company, category=category, level=level)

    job_data = get_job_data(api_url)
    
    print("Job Listings:")
    for job in job_data['results']:
        print(f"Title: {job.get('name', 'N/A')}")
        print(f"Company: {job['company'].get('name', 'N/A')}")
        if job.get('locations'):
            print(f"Location: {job['locations'][0].get('name', 'N/A')}")
        else:
            print("Location: N/A")
        if job.get('categories'):
            print(f"Category: {job['categories'][0].get('name', 'N/A')}")
        else:
            print("Category: N/A")
        if job.get('levels'):
            print(f"Level: {job['levels'][0].get('name', 'N/A')}")
        else:
            print("Level: N/A")
        print("-" * 30)

if __name__ == "__main__":
    main()