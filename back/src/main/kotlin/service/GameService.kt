package com.cybergames.service

import com.cybergames.entities.Game
import com.cybergames.entities.User
import com.cybergames.repository.GameRepository
import com.cybergames.repository.TeamRepository
import com.cybergames.repository.UserRepository
import com.cybergames.service.exceptions.GameNotFoundException
import com.cybergames.service.exceptions.TeamNotFoundException
import com.cybergames.service.exceptions.UserNotFoundException
import com.cybergames.service.mail.EmailSenderService
import org.springframework.stereotype.Service

@Service
class GameService(val gameRepository: GameRepository,
                  val teamRepository: TeamRepository) {

    fun create(game: Game): Long? {
        return gameRepository.save(game).id
    }

    fun addTeam(gameId: Long, teamId: Long){
        val team = teamRepository.findById(teamId).orElseThrow{ TeamNotFoundException() }
        var game = gameRepository.findById(gameId).orElseThrow{ GameNotFoundException() }
        game.teams.add(team)
        gameRepository.save(game)
    }

    fun findAll() : MutableIterable<Game> {
        return gameRepository.findAll()
    }
}