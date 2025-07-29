#!/usr/bin/env python3
"""
DOTUSDT Book Depth Data Analyzer
Analyzes the structure and content of the DOTUSDT order book data
"""

import pandas as pd
import os

def analyze_dotusdt_data():
    """Analyze the DOTUSDT book depth data structure."""
    file_path = os.path.expanduser('~/data/raw.binance-usdt-futures.BookDepth/date=2022-07-07/symbol=DOTUSDT/book_snapshot_5-20250707000000-0.parquet')
    
    print("📊 DOTUSDT Book Depth Data Analysis")
    print("=" * 60)
    
    # Load the data
    df = pd.read_parquet(file_path)
    
    print(f"📁 File: {os.path.basename(file_path)}")
    print(f"📏 Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
    print(f"💾 Size: {os.path.getsize(file_path) / (1024*1024):.2f} MB")
    print()
    
    # Display Table Format
    print("📊 TABLE FORMAT")
    print("-" * 60)
    print(f"{'Column':<20} {'Type':<10} {'Sample Value':<20} {'Description'}")
    print("-" * 60)
    
    # Core fields
    print(f"{'symbol':<20} {'object':<10} {'DOTUSDT':<20} {'Trading pair symbol'}")
    print(f"{'timestamp':<20} {'int64':<10} {'1657152000082000':<20} {'Unix timestamp (microseconds)'}")
    
    # Bid levels
    for i in range(1, 6):
        print(f"{f'bid_price_{i}':<20} {'float64':<10} {df[f'bid_price_{i}'].iloc[0]:<20.3f} {'Bid price level {i}'}")
        print(f"{f'bid_volume_{i}':<20} {'float64':<10} {df[f'bid_volume_{i}'].iloc[0]:<20.3f} {'Bid volume level {i}'}")
    
    # Ask levels
    for i in range(1, 6):
        print(f"{f'ask_price_{i}':<20} {'float64':<10} {df[f'ask_price_{i}'].iloc[0]:<20.3f} {'Ask price level {i}'}")
        print(f"{f'ask_volume_{i}':<20} {'float64':<10} {df[f'ask_volume_{i}'].iloc[0]:<20.3f} {'Ask volume level {i}'}")
    
    print()
    
    # Display Organizational Chart
    print("📋 ORGANIZATIONAL CHART")
    print("-" * 60)
    print("Order Book Snapshot Data")
    print("+-- symbol: \"DOTUSDT\"")
    print("+-- timestamp: Unix timestamp (microseconds)")
    print("+-- Bid Side (5 levels)")
    print("|   +-- bid_price_1: Best bid price")
    print("|   +-- bid_volume_1: Best bid volume")
    print("|   +-- bid_price_2: Second best bid price")
    print("|   +-- bid_volume_2: Second best bid volume")
    print("|   +-- bid_price_3: Third best bid price")
    print("|   +-- bid_volume_3: Third best bid volume")
    print("|   +-- bid_price_4: Fourth best bid price")
    print("|   +-- bid_volume_4: Fourth best bid volume")
    print("|   +-- bid_price_5: Fifth best bid price")
    print("|   +-- bid_volume_5: Fifth best bid volume")
    print("+-- Ask Side (5 levels)")
    print("    +-- ask_price_1: Best ask price")
    print("    +-- ask_volume_1: Best ask volume")
    print("    +-- ask_price_2: Second best ask price")
    print("    +-- ask_volume_2: Second best ask volume")
    print("    +-- ask_price_3: Third best ask price")
    print("    +-- ask_volume_3: Third best ask volume")
    print("    +-- ask_price_4: Fourth best ask price")
    print("    +-- ask_volume_4: Fourth best ask volume")
    print("    +-- ask_price_5: Fifth best ask price")
    print("    +-- ask_volume_5: Fifth best ask volume")
    
    print()
    
    # Time range analysis
    print("⏰ TIME RANGE ANALYSIS")
    print("-" * 60)
    start_time = pd.to_datetime(df['timestamp'].min(), unit='us')
    end_time = pd.to_datetime(df['timestamp'].max(), unit='us')
    print(f"Start: {start_time}")
    print(f"End: {end_time}")
    print(f"Duration: {end_time - start_time}")
    print(f"Total snapshots: {len(df):,}")
    
    # Price analysis
    print()
    print("💰 PRICE ANALYSIS")
    print("-" * 60)
    print(f"Bid price range: ${df['bid_price_1'].min():.3f} - ${df['bid_price_1'].max():.3f}")
    print(f"Ask price range: ${df['ask_price_1'].min():.3f} - ${df['ask_price_1'].max():.3f}")
    print(f"Spread range: ${(df['ask_price_1'] - df['bid_price_1']).min():.4f} - ${(df['ask_price_1'] - df['bid_price_1']).max():.4f}")
    
    print()
    print("✅ DOTUSDT analysis complete")

if __name__ == "__main__":
    analyze_dotusdt_data() 