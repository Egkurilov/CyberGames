package com.cybergames.controller

import com.cybergames.entities.Genre
import com.cybergames.entities.User
import com.cybergames.service.GenreService
import com.cybergames.service.UserService
import org.springframework.http.ResponseEntity
import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.*
import javax.websocket.server.PathParam

@RestController
@RequestMapping("/genre")
class GenreController(val genreService: GenreService) {
    @PostMapping("/add")
    fun add(@RequestBody genre: Genre) : ResponseEntity<Long>{
        return ResponseEntity.ok(genreService.create(genre))
    }

    @DeleteMapping("/{id}")
    fun delete(@PathParam("id") id : Long) : ResponseEntity<Long>{
        genreService.delete(id)
        return ResponseEntity.ok(id)
    }

    @GetMapping("/")
    fun all() : ResponseEntity<MutableIterable<Genre>>{
        return ResponseEntity.ok(genreService.findAll())
    }
}