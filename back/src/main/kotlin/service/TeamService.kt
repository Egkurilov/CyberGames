package com.cybergames.service

import com.cybergames.entities.Game
import com.cybergames.entities.Team
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
class TeamService(val teamRepository: TeamRepository) {

    fun create(team: Team): Long? {
        return teamRepository.save(team).id
    }

    fun findAll() : MutableIterable<Team> {
        return teamRepository.findAll()
    }
}