import imp
from rest_framework import status
from unittest import TestCase 
import requests
from django.conf import settings


class GetMetrics(TestCase):

    def setUp(self):
        self.params = {"start": "2021-01-01T09:00:00", "end": "2021-04-21T06:00:00"}
        self.request_data = { "time":"2021-03-20T11:58:5.173768Z","voltage":"13","current":"5"}


    def test_1_get_metrics(self):
        """
        Test Case for successful request
        """
        response = requests.get(settings.BASE_URL+"metrics", params=self.params)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Successfully get the data")
        
    def test_2_get_metrics(self):
        """
        Test Case for failed request
        """
        del self.params["start"]
        response = requests.get(settings.BASE_URL+"metrics", params=self.params)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, "start and end time series not provided")
        
    def test_3_post_metrics(self):
        """
        Test Case for successful request
        """
        response = requests.post(settings.BASE_URL+"metrics", json=self.request_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "metrics successfully created")
        
    def test_4_post_metrics(self):
        """
        Test Case for failed request 
        """
        self.request_data["current"]=""
        response = requests.post(settings.BASE_URL+"metrics", json=self.request_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, "Valid integer is required")
        