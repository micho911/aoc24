
def read_input(filename):
    with open(filename, 'r') as f:
        return f.read().strip()

def decode_disk_map(disk_map):
    blocks = []
    file_id = 0
    is_file = True
    
    for ch in disk_map:
        length = int(ch)
        content = str(file_id) if is_file else '.'
        blocks.extend([content] * length)
        
        if is_file:
            file_id += 1
        is_file = not is_file
    
    return blocks

def calculate_checksum(blocks):
    return sum(i * int(block) for i, block in enumerate(blocks) if block != '.')

def compact_disk_block_by_block(blocks):
    blocks = blocks.copy()
    
    while True:
        try:
            gap_index = blocks.index('.')
            if any(block != '.' for block in blocks[gap_index:]):
                rightmost_file = max(
                    (i for i in range(len(blocks)) if blocks[i] != '.'), 
                    default=-1
                )
                
                if rightmost_file != -1:
                    blocks[gap_index] = blocks[rightmost_file]
                    blocks[rightmost_file] = '.'
            else:
                break
        except ValueError:
            break
    
    return blocks

def get_files_info(blocks):
    file_positions = {}
    i = 0
    
    while i < len(blocks):
        if blocks[i] != '.':
            fid = int(blocks[i])
            start = i
            while i < len(blocks) and blocks[i] == str(fid):
                i += 1
            file_positions[fid] = (start, i - 1, i - start)
        else:
            i += 1
    
    return file_positions, max(file_positions.keys()) if file_positions else -1

def find_free_space_to_the_left(blocks, file_start, length):
    count = 0
    run_start = 0
    
    for i in range(file_start):
        if blocks[i] == '.':
            count += 1
        else:
            count = 0
            run_start = i + 1
        
        if count >= length:
            return run_start
    
    return -1

def move_file(blocks, fid, start, end, length):
    free_start = find_free_space_to_the_left(blocks, start, length)
    
    if free_start == -1:
        return
    
    file_blocks = blocks[start:end+1]
    blocks[start:end+1] = ['.'] * (end - start + 1)
    blocks[free_start:free_start+length] = file_blocks

def compact_disk_whole_file(blocks):
    blocks = blocks.copy()
    file_positions, max_fid = get_files_info(blocks)
    
    for fid in range(max_fid, -1, -1):
        if fid in file_positions:
            start, end, length = file_positions[fid]
            move_file(blocks, fid, start, end, length)
            file_positions, _ = get_files_info(blocks)
    
    return blocks

def main():
    input = read_input('./day9/day9.txt')
    original_blocks = decode_disk_map(input)

    block_by_block_result = compact_disk_block_by_block(original_blocks)
    block_by_block_checksum = calculate_checksum(block_by_block_result)

    whole_file_result = compact_disk_whole_file(original_blocks)
    whole_file_checksum = calculate_checksum(whole_file_result)

    print("\n--- Block-by-Block Compaction ---")
    print("Checksum:", block_by_block_checksum)

    print("\n--- Whole-File Compaction ---")
    print("Checksum:", whole_file_checksum)

if __name__ == "__main__":
    main()