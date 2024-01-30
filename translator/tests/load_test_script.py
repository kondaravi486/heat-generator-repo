#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import time
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument(
    "mode",
    help="Select the operation mode. Select `run` to run a load test and `cleanup` to perform a cleanup of all created helper- and meta-data",
    choices=['run', 'cleanup']
)

opt_group = parser.add_mutually_exclusive_group()
opt_group.add_argument("-n", type=int, help="Specify an amount of dummy data to be populated into the dataframe for the load test")

args = parser.parse_args()

def run_load_test(iterations):
    start_time = time.time()
    print(f"Running load test with {iterations} iterations...")
    # Perform load testing operations here
    total_sum = 0
    for i in range(iterations):
        # Example: Simulate some computational work
        result = compute(i)
        total_sum += result
    end_time = time.time()
    print(f"Load test completed in {end_time - start_time:.2f} seconds")
    print(f"Total sum computed: {total_sum}")

def compute(value):
    # Example: Simulate computational work by calculating the square of the value
    return value * value

def cleanup():
    print("Performing cleanup...")
    # Perform cleanup operations here
    try:
        subprocess.run(["docker", "exec", "heat-generator", "bash", "-c", "python3 /heat-generator-repo/translator/tests/load_test_script.py cleanup"])
        print("Cleanup completed successfully")
    except Exception as e:
        print(f"Error performing cleanup: {e}")

if args.mode == 'run':
    if args.n is not None:
        run_load_test(args.n)
    else:
        print("Please supply the -n argument")
elif args.mode == 'cleanup':
    cleanup()
else:
    print(f"Error: Unknown mode {args.mode}\n")
    parser.print_help()
