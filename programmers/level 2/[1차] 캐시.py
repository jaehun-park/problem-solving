def update_cache(cache_dict):
    for key in cache_dict:
        cache_dict[key] += 1


def LRU(cache_dict, new_cache, cache_size):
    if len(cache_dict) == cache_size:
        LRU_cache = None
        t = -1
        for cache in cache_dict:
            if cache_dict[cache] > t:
                t = cache_dict[cache]
                LRU_cache = cache
        del cache_dict[LRU_cache]
    cache_dict[new_cache] = 0
       
        
def solution(cache_size, cities):
    cache = dict()
    answer = 0
    
    for city in cities:
        city = city.lower()
        update_cache(cache)
        
        if city in cache:
            cache[city] = 0
            answer += 1
        else:
            if cache_size > 0:
                LRU(cache, city, cache_size)
            answer += 5
            
    return answer