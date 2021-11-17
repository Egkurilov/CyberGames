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
@RequestMapping
class TeamController(val teamService: TeamService) {
    @PostMapping("/team/add")
    fun add(@RequestBody team : Team) : ResponseEntity<Long>{
        return ResponseEntity.ok(teamService.create(team))
    }
}