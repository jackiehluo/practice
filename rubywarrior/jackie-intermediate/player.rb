class Player

  def initialize
    @retreated = false
  end

  def play_turn(warrior)
    direction = warrior.direction_of_stairs
    if not @retreated and warrior.health <= 5
      retreat(warrior)
      @retreated = true
    elsif @retreated and warrior.health < 10
      retreat(warrior)
    elsif check_enemies(warrior) != nil
      warrior.attack!(check_enemies(warrior))
    else
      warrior.walk!(direction)
    end
  end

  def retreat(warrior)
    if warrior.health + 2 >= 10
      @retreated = false
    endr
    if check_enemies(warrior) == nil
      warrior.rest!
    else
      warrior.walk!(:backward)
    end
  end

  def check_enemies(warrior)
    if warrior.feel(:left).enemy?
      direction = :left
    elsif warrior.feel(:right).enemy?
      direction = :right
    elsif warrior.feel(:forward).enemy?
      direction = :forward 
    elsif warrior.feel(:backward).enemy?
      direction = :backward
    else
      direction = nil
    end
    return direction
  end

end