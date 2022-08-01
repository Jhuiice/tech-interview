def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # can use a dict but can we do it in place?
    # can we use max()?

    num_dict = {}

    for num in nums:
        if num not in num_dict:
            num_dict[num] = 0

        num_dict[num] += 1

    kth_element_list = []
    print(max(num_dict.values()))
    for i in range(k):
        # * giving the number or frequency ot the key
        kth_element_list.append(max(num_dict.values()))
        print(kth_element_list[i])
        del num_dict[kth_element_list[i]]

    return kth_element_list


print(topKFrequent([1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 6], 2))
