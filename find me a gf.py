from TikTokApi import TikTokApi

def get_interests_from_user():
    print("Enter your interests, one per line. Type 'done' when you're finished.")
    interests = []
    while True:
        interest = input().strip()
        if interest.lower() == 'done':
            break
        interests.append(interest)
    return interests

def search_tiktok_users(interests, max_users=5):
    api = TikTokApi()
    users = set()
    
    for interest in interests:
        results = 10  # Adjust the number of results per interest if needed
        try:
            tiktoks = api.get_tiktoks_by_hashtag(hashtag=interest, count=results)
        except Exception as e:
            print(f"Error fetching TikToks for {interest}: {e}")
            continue
        
        for tiktok in tiktoks:
            user_id = tiktok['author']['id']
            user_name = tiktok['author']['uniqueId']
            users.add((user_id, user_name))
            
            if len(users) >= max_users:
                break
    
    return users

if __name__ == '__main__':
    interests = get_interests_from_user()
    tiktok_users = search_tiktok_users(interests)
    
    print("\nTikTok users with similar interests:")
    for user_id, user_name in tiktok_users:
        print(f'https://www.tiktok.com/@{user_name}')
