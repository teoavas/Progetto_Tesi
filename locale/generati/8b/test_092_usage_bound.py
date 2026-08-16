from funzione import usage_bound

def test_usage_bound_1():
    disk_sizes = [10, 20, 30]
    num_devices = 3
    raid_level = 'single'
    assert usage_bound(disk_sizes, num_devices, raid_level) == 10

def test_usage_bound_2():
    disk_sizes = [10, 20, 30]
    num_devices = 3
    raid_level = 'raid0'
    assert usage_bound(disk_sizes, num_devices, raid_level) == 15

def test_usage_bound_3():
    disk_sizes = [10, 20, 30]
    num_devices = 4
    raid_level = 'raid1'
    assert usage_bound(disk_sizes, num_devices, raid_level) == 5

def test_usage_bound_4():
    disk_sizes = [10, 20, 30]
    num_devices = 6
    raid_level = 'raid10'
    assert usage_bound(disk_sizes, num_devices, raid_level) == 15

def test_usage_bound_5():
    disk_sizes = [10, 20, 30]
    num_devices = 7
    raid_level = 'raid5'
    assert usage_bound(disk_sizes, num_devices, raid_level) == 12

def test_usage_bound_6():
    disk_sizes = [10, 20, 30]
    num_devices = 8
    raid_level = 'raid6'
    assert usage_bound(disk_sizes, num_devices, raid_level) == 11

def test_usage_bound_7():
    disk_sizes = [10, 20, 30]
    num_devices = 3
    raid_level = 'single'
    assert usage_bound(disk_sizes, num_devices, raid_level) == 10

def test_usage_bound_8():
    disk_sizes = [10, 20, 30]
    num_devices = 3
    raid_level = 'raid0'
    assert usage_bound(disk_sizes, num_devices, raid_level) == 15
