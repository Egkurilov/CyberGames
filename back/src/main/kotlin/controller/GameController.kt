package com.cybergames.controller

import com.cybergames.entities.Game
import com.cybergames.service.GameService
import org.springframework.http.ResponseEntity
import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.*
import javax.websocket.server.PathParam

@RestController
@RequestMapping
class GameController(val gameService: GameService) {
    @PostMapping("/game/add")
    fun add(@RequestBody game : Game) : ResponseEntity<Long> {
        return ResponseEntity.ok(gameService.create(game))
    }

    @GetMapping("/game")
    fun all() : ResponseEntity<MutableIterable<Game>> {
        return ResponseEntity.ok(gameService.findAll())
    }

    @GetMapping("/game/{gameId}/{teamId}")
    fun addTeam(@PathParam("gameId") gameId : Long, @PathParam("teamId") teamId : Long) : ResponseEntity<Any>{
        gameService.addTeam(gameId, teamId)
        return ResponseEntity.ok().build<Any>()
    }
}
