package com.cybergames.service

import com.cybergames.entities.Team
import com.cybergames.repository.TeamRepository
import com.cybergames.repository.UserRepository
import com.cybergames.service.exceptions.TeamNotFoundException
import com.cybergames.service.exceptions.UserNotFoundException
import org.springframework.stereotype.Service

@Service
class TeamService(val teamRepository: TeamRepository,
                  val userRepository: UserRepository) {

    fun create(team: Team): Long? {
        return teamRepository.save(team).id
    }

    fun setCaptain(teamId: Long, userId: Long){
        val team = teamRepository.findById(teamId).orElseThrow{ TeamNotFoundException(teamId)}
        val user = userRepository.findById(userId).orElseThrow{ UserNotFoundException(userId)}

        team.captain = user
        teamRepository.save(team)
    }

    fun addParticipant(teamId: Long, userId: Long){
        val team = teamRepository.findById(teamId).orElseThrow{ TeamNotFoundException(teamId)}
        val user = userRepository.findById(userId).orElseThrow{ UserNotFoundException(userId)}

        team.participants.add(user)
        teamRepository.save(team)
    }

    fun findAll() : MutableIterable<Team> {
        return teamRepository.findAll()
    }

    fun deleteParticipant(teamId: Long, userId: Long) {
        val team = teamRepository.findById(teamId).orElseThrow{ TeamNotFoundException(teamId)}
        val user = userRepository.findById(userId).orElseThrow{ UserNotFoundException(userId)}

        team.participants.remove(user)
        teamRepository.save(team)
    }
}