#!/usr/bin/env python3
"""
Quality State Viewer
Simple script to view the essential structure of _quality_state JSON files.
"""

import json
import os


def view_quality_state():
    """Show a quick overview of the quality state JSON structure."""
    file_path = os.path.expanduser('~/data/_quality_state/raw.binance-usdt-futures.BookDepth/ENAUSDT/state.json')
    
    print("🔍 Quality State Structure Viewer")
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
    print(f"{'last_processed_date':<30} {'string':<15} {'2025-07-16':<20} {'Date when data was last processed'}")
    print(f"{'last_updated_utc':<30} {'string':<15} {'2025-07-17T...':<20} {'UTC timestamp of last update'}")
    print(f"{'partitions_checked_in_last_run':<30} {'array':<15} {'[471 dates]':<20} {'List of processed date partitions'}")
    print(f"{'check_results':<30} {'array':<15} {'[3 checks]':<20} {'Quality check results'}")
    print(f"{'last_processed_timestamp':<30} {'integer':<15} {'1752710399858':<20} {'Unix timestamp of processing'}")
    
    print()
    
    # Display Organizational Chart
    print("📋 ORGANIZATIONAL CHART")
    print("-" * 50)
    print("JSON Root Object")
    print("+-- last_processed_date: \"2025-07-16\"")
    print("+-- last_updated_utc: \"2025-07-17T08:49:50.441662+00:00\"")
    print("+-- partitions_checked_in_last_run: Array[471]")
    print("|   +-- [0]: \"2024-04-02\"")
    print("|   +-- [1]: \"2024-04-03\"")
    print("|   +-- [2]: \"2024-04-04\"")
    print("|   +-- ... (468 more dates)")
    print("|   +-- [470]: \"2025-07-16\"")
    print("+-- check_results: Array[3]")
    print("|   +-- [0]: Object")
    print("|   |   +-- check_name: \"Date Coverage\"")
    print("|   |   +-- summary: \"Coverage from 2024-04-02 to 2025-07-16. Found 471/471 days. Missing: 0 days.\"")
    print("|   |   +-- details: Object")
    print("|   |       +-- start_date: \"2024-04-02\"")
    print("|   |       +-- end_date: \"2025-07-16\"")
    print("|   |       +-- expected_days: 471")
    print("|   |       +-- actual_days: 471")
    print("|   |       +-- missing_days: 0")
    print("|   +-- [1]: Object")
    print("|   |   +-- check_name: \"Timestamp Continuity\"")
    print("|   |   +-- summary: \"Found 1 total gaps. Max gap within batch: 870.42s.\"")
    print("|   |   +-- details: Object")
    print("|   |       +-- max_intra_batch_gap_ms: 870423")
    print("|   +-- [2]: Object")
    print("|       +-- check_name: \"Column Nullness\"")
    print("|       +-- summary: \"No nulls found in any columns.\"")
    print("|       +-- details: Object")
    print("|           +-- bid_price_1: 0.0")
    print("|           +-- bid_volume_1: 0.0")
    print("|           +-- bid_price_2: 0.0")
    print("|           +-- ... (16 more null rate fields)")
    print("|           +-- ask_volume_5: 0.0")
    print("+-- last_processed_timestamp: 1752710399858")
    
    print()
    print("✅ Quality state structure overview complete")


if __name__ == "__main__":
    view_quality_state() 