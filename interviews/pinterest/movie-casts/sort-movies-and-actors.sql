select movie.title, actor.name
from movie
left join movie_actor on movie.id = movie_actor.movie_id
left join actor on movie_actor.actor_id = actor.id
order by movie.title, actor.name;