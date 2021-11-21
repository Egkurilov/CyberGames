package com.cybergames.controller

import com.cybergames.entities.Team
import com.cybergames.entities.User
import com.cybergames.service.TeamService
import com.cybergames.service.UserService
import org.springframework.http.ResponseEntity
import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.*
import javax.websocket.server.PathParam

@RestController
@RequestMapping("/team")
class TeamController(val teamService: TeamService) {
    @PostMapping("/add")
    fun add(@RequestBody team : Team) : ResponseEntity<Long>{
        return ResponseEntity.ok(teamService.create(team))
    }

    @GetMapping("/adduser/{teamid}/{userid}")
    fun addUser(@PathParam("teamid") teamId : Long,
                @PathParam("userid") userId:  Long ) : ResponseEntity<Long> {
        teamService.addParticipant(teamId, userId)
        return ResponseEntity.ok(teamId)
    }

    @GetMapping("/deleteuser/{teamid}/{userid}")
    fun deleteUser(@PathParam("teamid") teamId : Long,
                @PathParam("userid") userId:  Long ) : ResponseEntity<Long> {
        teamService.deleteParticipant(teamId, userId)
        return ResponseEntity.ok(teamId)
    }

    @GetMapping("/setcaptain/{teamid}/{userid}")
    fun setCaptain(@PathParam("teamid") teamId : Long,
                   @PathParam("userid") userId:  Long ) : ResponseEntity<Long> {
        teamService.setCaptain(teamId, userId)
        return ResponseEntity.ok(teamId)
    }
}