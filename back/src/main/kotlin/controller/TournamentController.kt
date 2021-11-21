package com.cybergames.controller

import com.cybergames.entities.Tournament
import com.cybergames.service.TournamentService
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.*
import javax.websocket.server.PathParam

@RestController
@RequestMapping("/tournament")
class TournamentController(val tournamentService: TournamentService) {
    @PostMapping("/add")
    fun add(@RequestBody tournament : Tournament) : ResponseEntity<Long>{
        return ResponseEntity.ok(tournamentService.create(tournament))
    }

    @GetMapping
    fun all() : ResponseEntity<MutableIterable<Tournament>>{
        return ResponseEntity.ok(tournamentService.findAll())
    }

    @GetMapping("/addteam/{tournamentId}/{teamId}")
    fun addTeam(@PathParam("tournamentId") tournamentId : Long,
                @PathParam("teamId") teamId : Long, ) : ResponseEntity<Long>{
        tournamentService.addTeam(tournamentId, teamId)
        return ResponseEntity.ok(tournamentId)
    }
}