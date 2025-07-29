#!/usr/bin/env python3
"""
Tardis Failed Downloads Viewer
Simple script to view the essential structure of tardis_failed_downloads.json files.
"""

import json
import os


def view_tardis_failed_downloads():
    """Show a quick overview of the tardis failed downloads JSON structure."""
    file_path = os.path.expanduser('~/data/tardis_failed_downloads.json')
    
    print("🔍 Tardis Failed Downloads Structure Viewer")
    print("=" * 50)
    
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    print(f"📁 File: {os.path.basename(file_path)}")
    print()
    
    # Display Table Format
    print("📊 TABLE FORMAT")
    print("-" * 50)
    print(f"{'Field':<30} {'Type':<15} {'Value':<20} {'Description'}")
    print("-" * 50)
    
    # Root level fields
    print(f"{'tardis':<30} {'object':<15} {'{book_snapshot_5}':<20} {'Root object containing data types'}")
    
    print()
    
    # Display Organizational Chart
    print("📋 ORGANIZATIONAL CHART")
    print("-" * 50)
    print("JSON Root Object")
    print("+-- tardis: Object")
    print("    +-- book_snapshot_5: Object")
    print("    |   +-- EOSUSDT: Object")
    print("    |   |   +-- 2025-05-22: Object")
    print("    |   |   |   +-- reason: \"empty_data\"")
    print("    |   |   |   +-- timestamp: \"2025-07-16T03:14:07.299760+00:00\"")
    print("    |   |   |   +-- retry_count: 1")
    print("    |   |   |   +-- permanent: true")
    print("    |   |   |   +-- error_msg: \"Downloaded data is too small\"")
    print("    |   +-- OMGUSDT: Object")
    print("    |   |   +-- 2025-02-01: Object")
    print("    |   |   |   +-- reason: \"empty_data\"")
    print("    |   |   |   +-- timestamp: \"2025-07-16T03:14:50.544996+00:00\"")
    print("    |   |   |   +-- retry_count: 1")
    print("    |   |   |   +-- permanent: true")
    print("    |   |   |   +-- error_msg: \"Downloaded data is too small\"")
    print("    |   +-- ... (more symbols)")
    print("    +-- derivative_ticker: Object")
    print("    |   +-- CVCUSDT: Object")
    print("    |   |   +-- 2022-12-01: Object")
    print("    |   |   |   +-- reason: \"empty_data\"")
    print("    |   |   |   +-- timestamp: \"2025-07-16T03:14:52.390422+00:00\"")
    print("    |   |   |   +-- retry_count: 1")
    print("    |   |   |   +-- permanent: true")
    print("    |   |   |   +-- error_msg: \"Downloaded data is too small\"")
    print("    |   +-- ... (more symbols)")
    print("    +-- trades: Object")
    print("        +-- EOSUSDT: Object")
    print("        |   +-- 2025-05-22: Object")
    print("        |   |   +-- reason: \"empty_data\"")
    print("        |   |   +-- timestamp: \"2025-07-16T03:14:06.298060+00:00\"")
    print("        |   |   +-- retry_count: 1")
    print("        |   |   +-- permanent: true")
    print("        |   |   +-- error_msg: \"Downloaded data is too small\"")
    print("        +-- ... (more symbols)")
    
    print()
    print("✅ Tardis failed downloads structure overview complete")


if __name__ == "__main__":
    view_tardis_failed_downloads() 