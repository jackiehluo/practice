class Player
  def play_turn(warrior)
    direction = warrior.direction_of_stairs
    warrior.walk!(direction)
  end
end