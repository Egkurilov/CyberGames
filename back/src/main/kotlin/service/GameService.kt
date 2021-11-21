package com.cybergames.service

import com.cybergames.entities.Game
import com.cybergames.repository.GameRepository
import com.cybergames.repository.TeamRepository
import com.cybergames.service.exceptions.GameNotFoundException
import com.cybergames.service.exceptions.TeamNotFoundException
import org.springframework.stereotype.Service

@Service
class GameService(val gameRepository: GameRepository,
                  val teamRepository: TeamRepository) {

    fun create(game: Game): Long? {
        return gameRepository.save(game).id
    }

    fun addTeam(gameId: Long, teamId: Long){
        val team = teamRepository.findById(teamId).orElseThrow{ TeamNotFoundException(teamId) }
        var game = gameRepository.findById(gameId).orElseThrow{ GameNotFoundException(gameId) }
        game.teams.add(team)
        gameRepository.save(game)
    }

    fun findAll() : MutableIterable<Game> {
        return gameRepository.findAll()
    }
}