from playwright.sync_api import sync_playwright
import openpyxl
import os
import csv

wb = openpyxl.Workbook()
ws = wb.active
ws.append(["Title", "Price", "Location", "Bedrooms", "Bathrooms", "Garage","Property Type", "Size", "URL"])

all_property = []
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://stately-residence-search.lovable.app/properties")
    page.wait_for_timeout(3000)
 
    links = page.locator("a[href^='/properties/']").all()
    property_links = []
    for link in links:
        href = link.get_attribute("href")
        if href and href != "/properties":
            complete_url = f"https://stately-residence-search.lovable.app{href}"
            if complete_url not in property_links:
                property_links.append(complete_url)

    print(f"Found {len(property_links)} properties")
    
    for property_url in property_links:
        try:
            page.goto(property_url)
            page.wait_for_timeout(3000)

            Title= page.locator("h1").first.inner_text()
            Price = page.locator("p.font-display").first.inner_text()
            location = page.locator("p.text-muted-foreground.mt-4").inner_text()
            property_type = page.locator("p.eyebrow").inner_text()
            dds= page.locator("dd").all()
            bathrooms = dds[0].inner_text() if len(dds)> 0 else "N/A"
            garage = dds[1].inner_text() if len(dds)> 1 else "N/A"
            bedrooms = dds[2].inner_text() if len(dds)> 2 else "N/A"
            size = dds[3].inner_text() if len(dds)> 3 else "N/A"

            print(f"Successfully scraped: {Title}")
            row =[Title, Price, location, bedrooms, bathrooms, garage, property_type, size,property_url]
            ws.append(row)
            all_property.append(row)

        except Exception as e:
            print(f"Error: {property_url} → {e}")
    browser.close()  # ✅ inside the with block


desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "Ah.xlsx")
wb.save(desktop_path)
print("Saved to Excel")

desktop_path_csv= os.path.join(os.path.expanduser("~"), "Desktop", "data.csv")
with open(desktop_path_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Location", "Bedrooms", "Bathrooms", "Garage","Property Type", "Size", "URL"])
    for row in all_property:
        writer.writerow(row)

print(f"CSV saved to: {desktop_path_csv}")
