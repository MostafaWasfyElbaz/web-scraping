# importing libraries

from bs4 import BeautifulSoup
import requests
import csv

while True:

    # get GPU version

    gpu = int(input("input the gpu u need: "))

    # request the page

    page_request = requests.get(f"https://www.newegg.com/p/pl?d=gtx+{gpu}&Order=1")

    def main(page):

        # use Beautiful soup to converting byte code

        soup = BeautifulSoup(page.content, "lxml")

        # get all GPU containers

        gpu_containers = soup.find_all("div", {'class': 'item-container'})

        def gpu_info(gpu_container):

            # make list for GPUs

            gpu_list = []

            # get the GPUs' names and prices

            for i in range(len(gpu_container)):

                # get GPUs' names

                gpu_title = gpu_container[i].find("a", {'class': 'item-title'}).text

                # get GPUs' price

                gpu_price = gpu_container[i].find("li", {'class': 'price-current'}).strong.text

                # put the results in list

                gpu_list.append({"gpu names": gpu_title, "gpu prices": "$" + gpu_price})

            # get key of dictionary

            keys = gpu_list[0].keys()

            # write in csv file

            with open('S:\GPU_Details.csv', 'w') as f:
                writer = csv.DictWriter(f, keys)

                # write header

                writer.writeheader()

                # write rows

                writer.writerows(gpu_list)

            # print file created

            print("file created")

        # call gpu_info function

        gpu_info(gpu_containers)

    # call gpu_info function

    main(page_request)
