"""
EvacAid API Example
Demonstrates how to interact with the EvacAid platform API.

Entities included:
- Contacts
- Shelters
- Emergency Settings
- Family Members
"""

import requests
import os

BASE_URL = "https://app.base44.com/api"
APP_ID = "680e0a913bf6568230dcb0c9"

API_KEY = os.getenv("EVACAID_API_KEY")

HEADERS = {
    "api_key": API_KEY,
    "Content-Type": "application/json"
}


def make_api_request(api_path, method="GET", data=None):
    url = f"{BASE_URL}/{api_path}"

    if method == "GET":
        response = requests.get(url, headers=HEADERS, params=data)
    else:
        response = requests.request(method, url, headers=HEADERS, json=data)

    response.raise_for_status()
    return response.json()


# -------------------------
# CONTACTS
# -------------------------

def get_contacts():
    return make_api_request(f"apps/{APP_ID}/entities/Contact")


def update_contact(contact_id, update_data):
    return make_api_request(
        f"apps/{APP_ID}/entities/Contact/{contact_id}",
        method="PUT",
        data=update_data
    )


# -------------------------
# SHELTERS
# -------------------------

def get_shelters():
    return make_api_request(f"apps/{APP_ID}/entities/Shelter")


def update_shelter(shelter_id, update_data):
    return make_api_request(
        f"apps/{APP_ID}/entities/Shelter/{shelter_id}",
        method="PUT",
        data=update_data
    )


# -------------------------
# EMERGENCY SETTINGS
# -------------------------

def get_emergency_settings():
    return make_api_request(f"apps/{APP_ID}/entities/EmergencySettings")


def update_emergency_settings(settings_id, update_data):
    return make_api_request(
        f"apps/{APP_ID}/entities/EmergencySettings/{settings_id}",
        method="PUT",
        data=update_data
    )


# -------------------------
# FAMILY MEMBERS
# -------------------------

def get_family_members():
    return make_api_request(f"apps/{APP_ID}/entities/FamilyMember")


def update_family_member(member_id, update_data):
    return make_api_request(
        f"apps/{APP_ID}/entities/FamilyMember/{member_id}",
        method="PUT",
        data=update_data
    )


# -------------------------
# Example Usage
# -------------------------

if __name__ == "__main__":

    print("Fetching contacts...")
    contacts = get_contacts()
    print(contacts)

    print("\nFetching shelters...")
    shelters = get_shelters()
    print(shelters)

    print("\nFetching emergency settings...")
    settings = get_emergency_settings()
    print(settings)

    print("\nFetching family members...")
    members = get_family_members()
    print(members)

    print("\nEvacAid API demo completed.")
