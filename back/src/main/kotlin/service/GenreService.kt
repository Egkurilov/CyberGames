package com.cybergames.service

import com.cybergames.entities.Game
import com.cybergames.entities.Genre
import com.cybergames.entities.Tournament
import com.cybergames.entities.User
import com.cybergames.repository.*
import com.cybergames.service.exceptions.GameNotFoundException
import com.cybergames.service.exceptions.TeamNotFoundException
import com.cybergames.service.exceptions.UserNotFoundException
import com.cybergames.service.mail.EmailSenderService
import org.springframework.stereotype.Service

@Service
class GenreService(val genreRepository: GenreRepository) {

    fun create(genre: Genre): Long? {
        return genreRepository.save(genre).id
    }

    fun delete(id : Long) {
        genreRepository.deleteById(id)
    }

    fun findAll() : MutableIterable<Genre> {
        return genreRepository.findAll()
    }
}