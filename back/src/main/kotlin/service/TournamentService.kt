package com.cybergames.service

import com.cybergames.entities.Game
import com.cybergames.entities.Tournament
import com.cybergames.entities.User
import com.cybergames.repository.GameRepository
import com.cybergames.repository.TeamRepository
import com.cybergames.repository.TournamentRepository
import com.cybergames.repository.UserRepository
import com.cybergames.service.exceptions.GameNotFoundException
import com.cybergames.service.exceptions.TeamNotFoundException
import com.cybergames.service.exceptions.UserNotFoundException
import com.cybergames.service.mail.EmailSenderService
import org.springframework.stereotype.Service

@Service
class TournamentService(val tournamentRepository: TournamentRepository) {

    fun create(tournament: Tournament): Long? {
        return tournamentRepository.save(tournament).id
    }

    fun findAll() : MutableIterable<Tournament> {
        return tournamentRepository.findAll()
    }
}