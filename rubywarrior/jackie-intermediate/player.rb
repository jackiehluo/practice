class Player

  def initialize
    @retreated = false
    @captives = true
  end

  def play_turn(warrior)
    direction = warrior.direction_of_stairs
    if not @retreated and warrior.health < 10
      retreat(warrior)
      @retreated = true
    elsif @retreated and warrior.health < 20
      retreat(warrior)
    elsif @captives and not check_captives(warrior).empty?
      warrior.rescue!(check_captives(warrior)[0])
    elsif not check_enemies(warrior).empty?
      if check_enemies(warrior).length > 1
        warrior.bind!(check_enemies(warrior)[0])
      else
        warrior.attack!(check_enemies(warrior)[0])
      end
    elsif not @captives and not check_captives(warrior).empty?
      warrior.attack!(check_captives(warrior)[0])
    else
      warrior.walk!(direction)
    end
  end

  def retreat(warrior)
    if warrior.health + 3 >= 20
      @retreated = false
    end
    if check_enemies(warrior).empty?
      warrior.rest!
    else
      if warrior.feel(:left).empty? and warrior.direction_of_stairs != :left
        warrior.walk!(:left)
      elsif warrior.feel(:right).empty? and warrior.direction_of_stairs != :right
        warrior.walk!(:right)
      elsif warrior.feel(:forward).empty? and warrior.direction_of_stairs != :forward
        warrior.walk!(:forward)
      else
        warrior.walk!(:backward)
      end
    end
  end

  def check_enemies(warrior)
    directions = []
    if warrior.feel(:left).enemy?
      directions.push(:left)
    end
    if warrior.feel(:right).enemy?
      directions.push(:right)
    end
    if warrior.feel(:forward).enemy?
      directions.push(:forward)
    end
    if warrior.feel(:backward).enemy?
      directions.push(:backward)
    end
    return directions
  end

  def check_captives(warrior)
    @captives = false
    directions = []
    if warrior.feel(:left).captive?
      directions.push(:left)
    end
    if warrior.feel(:right).captive?
      directions.push(:right)
    end
    if warrior.feel(:forward).captive?
      directions.push(:forward)
    end
    if warrior.feel(:backward).captive?
      directions.push(:backward)
    end
    return directions
  end

end