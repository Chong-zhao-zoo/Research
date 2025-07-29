#!/usr/bin/env python3
"""
Binance Failed Downloads Viewer
Simple script to view the essential structure of binance_failed_downloads.json files.
"""

import json
import os


def view_binance_failed_downloads():
    """Show a quick overview of the binance failed downloads JSON structure."""
    file_path = os.path.expanduser('~/data/binance_failed_downloads.json')
    
    print("🔍 Binance Failed Downloads Structure Viewer")
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
    print(f"{'binance':<30} {'object':<15} {'{metrics}':<20} {'Root object containing data sources'}")
    
    print()
    
    # Display Organizational Chart
    print("📋 ORGANIZATIONAL CHART")
    print("-" * 50)
    print("JSON Root Object")
    print("+-- binance: Object")
    print("    +-- metrics: Object")
    print("        +-- BTCUSDT: Object")
    print("        |   +-- 2025-07-15: Object")
    print("        |   |   +-- reason: \"no_data\"")
    print("        |   |   +-- timestamp: \"2025-07-16T03:21:03.447082+00:00\"")
    print("        |   |   +-- retry_count: 1")
    print("        |   |   +-- permanent: true")
    print("        |   |   +-- error_msg: \"No data available (404)\"")
    print("        |   +-- 2025-07-16: Object")
    print("        |       +-- reason: \"no_data\"")
    print("        |       +-- timestamp: \"2025-07-17T02:52:47.655582+00:00\"")
    print("        |       +-- retry_count: 1")
    print("        |       +-- permanent: true")
    print("        |       +-- error_msg: \"No data available (404)\"")
    print("        +-- BTCDOMUSDT: Object")
    print("        |   +-- 2025-07-15: Object")
    print("        |   |   +-- reason: \"no_data\"")
    print("        |   |   +-- timestamp: \"2025-07-16T03:22:08.873557+00:00\"")
    print("        |   |   +-- retry_count: 1")
    print("        |   |   +-- permanent: true")
    print("        |   |   +-- error_msg: \"No data available (404)\"")
    print("        |   +-- 2025-07-16: Object")
    print("        |       +-- reason: \"no_data\"")
    print("        |       +-- timestamp: \"2025-07-17T02:52:47.436509+00:00\"")
    print("        |       +-- retry_count: 1")
    print("        |       +-- permanent: true")
    print("        |       +-- error_msg: \"No data available (404)\"")
    print("        +-- ... (more symbols)")
    
    print()
    print("✅ Binance failed downloads structure overview complete")


if __name__ == "__main__":
    view_binance_failed_downloads() 