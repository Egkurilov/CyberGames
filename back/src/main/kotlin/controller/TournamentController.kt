package com.cybergames.controller

import com.cybergames.entities.Tournament
import com.cybergames.service.TournamentService
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping
class TournamentController(val tournamentService: TournamentService) {
    @PostMapping("/tournament/add")
    fun add(@RequestBody tournament : Tournament) : ResponseEntity<Long>{
        return ResponseEntity.ok(tournamentService.create(tournament))
    }

    @GetMapping("/tournament")
    fun all() : ResponseEntity<MutableIterable<Tournament>>{
        return ResponseEntity.ok(tournamentService.findAll())
    }
}