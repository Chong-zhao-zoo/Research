#!/usr/bin/env python3
"""
Mark Price Data File Analyzer
Analyzes the structure and statistics of mark price parquet files with comprehensive details
"""

import os
import sys
import json

def analyze_markprice_file(file_path):
    """Analyze mark price parquet file structure and statistics."""
    print("🔍 Mark Price Data File Analysis")
    print("=" * 60)
    print(f"File: {os.path.basename(file_path)}")
    print(f"Full Path: {file_path}")
    print()
    
    # Basic file statistics
    file_size_mb = os.path.getsize(file_path) / (1024*1024)
    print("📊 FILE STATISTICS")
    print("-" * 60)
    print(f"File Size: {file_size_mb:.2f} MB")
    print(f"File Size: {file_size_mb * 1024:.0f} KB")
    print(f"File Size: {os.path.getsize(file_path):,} bytes")
    print()
    
    # Try to get basic info about the file
    try:
        # Check if we can read the file
        with open(file_path, 'rb') as f:
            header = f.read(100)
            
            # Try to find parquet magic number
            if b'PAR1' in header:
                print("✅ Valid Parquet file (contains PAR1 magic number)")
            else:
                print("❓ File format unclear")
                
    except Exception as e:
        print(f"Error reading file: {e}")
    
    print()
    
    # Parse filename for information
    filename = os.path.basename(file_path)
    parts = filename.replace('.parquet', '').split('-')
    
    if len(parts) >= 3:
        print("📝 FILENAME ANALYSIS")
        print("-" * 60)
        print(f"Data Type: {parts[0]}")  # derivative_ticker
        print(f"Timestamp: {parts[1]}")  # 20250707000000
        print(f"File Index: {parts[2]}")  # 0
        
        # Parse timestamp
        timestamp = parts[1]
        if len(timestamp) == 14:
            year = timestamp[:4]
            month = timestamp[4:6]
            day = timestamp[6:8]
            hour = timestamp[8:10]
            minute = timestamp[10:12]
            second = timestamp[12:14]
            print(f"Parsed Date: {year}-{month}-{day} {hour}:{minute}:{second}")
    
    print()
    
    # Try to get row count and column info if pandas is available
    try:
        import pandas as pd
        df = pd.read_parquet(file_path)
        
        print("📈 DATA STATISTICS")
        print("-" * 60)
        print(f"Total Rows (Price Updates): {len(df):,}")
        print(f"Total Columns: {len(df.columns)}")
        print(f"Data Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
        
        # Time range if timestamp column exists
        if 'timestamp' in df.columns:
            start_time = pd.to_datetime(df['timestamp'].min(), unit='us')
            end_time = pd.to_datetime(df['timestamp'].max(), unit='us')
            duration = end_time - start_time
            print(f"Time Range: {start_time} to {end_time}")
            print(f"Duration: {duration}")
            print(f"Average updates per second: {len(df) / (24*60*60):.1f}")
        
        print()
        
        # Display Organizational Chart
        print("📋 ORGANIZATIONAL CHART")
        print("-" * 60)
        print("Mark Price Parquet File Structure")
        print("+-- File Metadata")
        print("|   +-- Format: Parquet")
        print("|   +-- Size: {:.2f} MB".format(file_size_mb))
        print("|   +-- Price Updates: {:,}".format(len(df)))
        print("|   +-- Columns: {}".format(len(df.columns)))
        print("|   +-- Compression: Columnar")
        print("+-- Data Columns")
        
        # Group columns by type
        price_cols = [col for col in df.columns if 'price' in col]
        time_cols = [col for col in df.columns if 'time' in col or 'timestamp' in col]
        other_cols = [col for col in df.columns if 'price' not in col and 'time' not in col and 'timestamp' not in col]
        
        print("|   +-- Core Fields")
        for col in other_cols:
            sample_val = str(df[col].iloc[0])[:20] if len(df) > 0 else "N/A"
            print("|   |   +-- {}: {} (sample: {})".format(col, df[col].dtype, sample_val))
        
        print("|   +-- Price Information")
        for col in price_cols:
            sample_val = df[col].iloc[0] if len(df) > 0 else "N/A"
            print("|   |   +-- {}: {} (sample: {:.6f})".format(col, df[col].dtype, sample_val))
        
        print("|   +-- Time Information")
        for col in time_cols:
            sample_val = str(df[col].iloc[0])[:20] if len(df) > 0 else "N/A"
            print("|   |   +-- {}: {} (sample: {})".format(col, df[col].dtype, sample_val))
        
        print("+-- Data Characteristics")
        print("|   +-- Storage: Columnar (Parquet)")
        print("|   +-- Compression: High efficiency")
        print("|   +-- Query Performance: Fast column access")
        print("|   +-- Schema: Preserved data types")
        
    except ImportError as e:
        print(f"❌ Pandas not available - cannot read parquet file: {e}")
        print("📋 ORGANIZATIONAL CHART")
        print("-" * 60)
        print("Mark Price Parquet File Structure")
        print("+-- File Metadata")
        print("|   +-- Format: Parquet")
        print("|   +-- Size: {:.2f} MB".format(file_size_mb))
        print("|   +-- Price Updates: N/A (pandas not available)")
        print("|   +-- Compression: Columnar")
        print("+-- Data Structure")
        print("|   +-- Mark Price Data")
        print("|   |   +-- Symbol: Trading pair identifier")
        print("|   |   +-- Timestamp: Unix timestamp (microseconds)")
        print("|   |   +-- Mark Price: Current mark price")
        print("|   |   +-- Index Price: Reference index price")
        print("|   |   +-- Funding Rate: Current funding rate")
        print("|   |   +-- Next Funding Time: Next funding calculation")
        print("+-- Storage Benefits")
        print("|   +-- Columnar storage for fast queries")
        print("|   +-- High compression ratio")
        print("|   +-- Schema preservation")
    except Exception as e:
        print(f"❌ Error reading parquet file: {e}")
        print("📋 ORGANIZATIONAL CHART")
        print("-" * 60)
        print("Mark Price Parquet File Structure")
        print("+-- File Metadata")
        print("|   +-- Format: Parquet")
        print("|   +-- Size: {:.2f} MB".format(file_size_mb))
        print("|   +-- Price Updates: N/A (error reading file)")
        print("|   +-- Compression: Columnar")
        print("+-- Data Structure")
        print("|   +-- Mark Price Data")
        print("|   |   +-- Symbol: Trading pair identifier")
        print("|   |   +-- Timestamp: Unix timestamp (microseconds)")
        print("|   |   +-- Mark Price: Current mark price")
        print("|   |   +-- Index Price: Reference index price")
        print("|   |   +-- Funding Rate: Current funding rate")
        print("|   |   +-- Next Funding Time: Next funding calculation")
        print("+-- Storage Benefits")
        print("|   +-- Columnar storage for fast queries")
        print("|   +-- High compression ratio")
        print("|   +-- Schema preservation")
    
    print()
    print("✅ Mark price data analysis complete")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = "~/data/raw.binance-usdt-futures.MarkPrice/date=2022-07-07/symbol=BTCUSDT/derivative_ticker-20250707000000-0.parquet"
    
    analyze_markprice_file(os.path.expanduser(file_path)) 