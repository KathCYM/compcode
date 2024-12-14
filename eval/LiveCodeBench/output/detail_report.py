import ast
import argparse

def calculate_averages(filename):
    # Dictionaries to store cumulative sums and counts
    difficulty_sums = {'easy': {'pass_1': 0, 'count': 0},
                       'medium': {'pass_1': 0, 'count': 0},
                       'hard': {'pass_1': 0, 'count': 0}}
    
    platform_sums = {'codeforces': {'pass_1': 0, 'count': 0},
                     'leetcode': {'pass_1': 0, 'count': 0},
                     'atcoder': {'pass_1': 0, 'count': 0}}
    
    # Read each line in the file
    with open(filename, 'r') as file:
        for line in file:
            # Convert line to dictionary using ast.literal_eval
            data = ast.literal_eval(line.strip())
            # Update difficulty sums
            difficulty = data.get('difficulty', 'unknown')
            if difficulty in difficulty_sums:
                difficulty_sums[difficulty]['pass_1'] += data.get('pass@1')
                difficulty_sums[difficulty]['count'] += 1
            
            # Update platform sums
            platform = data.get('platform', 'unknown')
            if platform in platform_sums:
                platform_sums[platform]['pass_1'] += data.get('pass@1')
                platform_sums[platform]['count'] += 1
    
    # Calculate averages for pass_1 only
    difficulty_averages = {diff: difficulty_sums[diff]['pass_1'] / difficulty_sums[diff]['count']
                           for diff in difficulty_sums if difficulty_sums[diff]['count'] > 0}
    
    platform_averages = {plat: platform_sums[plat]['pass_1'] / platform_sums[plat]['count']
                         for plat in platform_sums if platform_sums[plat]['count'] > 0}
    
    return difficulty_averages, platform_averages

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate average pass_1 by difficulty and platform")
    parser.add_argument("filename", type=str, help="Path to the data file")
    args = parser.parse_args()

    difficulty_avg, platform_avg = calculate_averages(args.filename)
    print("Difficulty Averages (pass_1):", difficulty_avg)
    print("Platform Averages (pass_1):", platform_avg)
