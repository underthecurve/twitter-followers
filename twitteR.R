library(twitteR)
library(data.table)

# Replace XXXXXXXX with your information

api_key <- "XXXXXXXX"
api_secret <- "XXXXXXXX"

access_token <- "XXXXXXXX"
access_secret <- "XXXXXXXX"

setup_twitter_oauth(api_key, api_secret, access_token, access_secret)

user <- getUser("christinezhang") # replace with username you want
user_follower_IDs <- user$getFollowers(retryOnRateLimit=180)
user_followers <- rbindlist(lapply(user_follower_IDs, as.data.frame))

# View(user_followers[,c('name', 'screenName', 'location')])

# write.csv(user_followers, 'followers.csv') # to save to .csv file

# friends_ids <- user$getFriends(retryOnRateLimit=180) # to get people the user is following
# friends_ids_df = rbindlist(lapply(friends_ids,as.data.frame))

