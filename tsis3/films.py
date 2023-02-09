def good_movie(**movie): 
     if movie["imdb"] >= 5.5: 
         return True 
     else: 
         return False 

  
 def by_cat(movie, cat): 
     sublist = [] 
     for i in movie: 
         if i["category"].lower() == cat.lower(): 
             sublist.append(i) 
     return sublist 
  
 def average_score(movie): 
     sum = 0 
     for i in movie: 
         sum += i["imdb"] 
     return sum / len(movie) 
  
 def average_score_by_cat(movie, cat): 
     sum = 0 
     cnt = 0 
     for i in movie: 
         if i["category"].lower() == cat.lower(): 
             sum += i["imdb"] 
             cnt += 1 
     return sum / cnt 
      
 # Dictionary of movies 
  
 movies = [ 
 { 
 "name": "Usual Suspects",  
 "imdb": 7.0, 
 "category": "Thriller" 
 }, 
 { 
 "name": "Hitman", 
 "imdb": 6.3, 
 "category": "Action" 
 }, 
 { 
 "name": "Dark Knight", 
 "imdb": 9.0, 
 "category": "Adventure" 
 }, 
 { 
 "name": "The Help", 
 "imdb": 8.0, 
 "category": "Drama" 
 }, 
 { 
 "name": "The Choice", 
 "imdb": 6.2, 
 "category": "Romance" 
 }, 
 { 
 "name": "Colonia", 
 "imdb": 7.4, 
 "category": "Romance" 
 }, 
 { 
 "name": "Love", 
 "imdb": 6.0, 
 "category": "Romance" 
 }, 
 { 
 "name": "Bride Wars", 
 "imdb": 5.4, 
 "category": "Romance" 
 }, 
 { 
 "name": "AlphaJet", 
 "imdb": 3.2, 
 "category": "War" 
 }, 
 { 
 "name": "Ringing Crime", 
 "imdb": 4.0, 
 "category": "Crime" 
 }, 
 { 
 "name": "Joking muck", 
 "imdb": 7.2, 
 "category": "Comedy" 
 }, 
 { 
 "name": "What is the name", 
 "imdb": 9.2, 
 "category": "Suspense" 
 }, 
 { 
 "name": "Detective", 
 "imdb": 7.0, 
 "category": "Suspense" 
 }, 
 { 
 "name": "Exam", 
 "imdb": 4.2, 
 "category": "Thriller" 
 }, 
 { 
 "name": "We Two", 
 "imdb": 7.2, 
 "category": "Romance" 
 } 
 ] 
 # if good_movie(**movies[-2]): 
 #     print("good") 
 # else: 
 #     print("Not recommend") 
  
 # print(sub_list(movies)) 
  
 # print(average_score(movies[1:5])) 
 print(average_score_by_cat(movies, "romance")) ``
