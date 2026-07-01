import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { libraryApi } from '../api/libraryApi'

export function useBooks() {
  return useQuery({
    queryKey: ['books', 'list'],
    queryFn: () => libraryApi.getBooks(),
    staleTime: 1000 * 60 * 5,
  })
}

export function useBookDetail(id: string) {
  return useQuery({
    queryKey: ['books', 'detail', id],
    queryFn: () => libraryApi.getBook(id),
    enabled: Boolean(id),
    staleTime: 1000 * 60 * 5,
  })
}

export function useCreateBook() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: libraryApi.createBook,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['books', 'list'] })
    },
  })
}

export function useUpdateBook() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: ({ id, data }: { id: string; data: Parameters<typeof libraryApi.updateBook>[1] }) => 
      libraryApi.updateBook(id, data),
    onSuccess: (_, variables) => {
      queryClient.invalidateQueries({ queryKey: ['books', 'list'] })
      queryClient.invalidateQueries({ queryKey: ['books', 'detail', variables.id] })
    },
  })
}

export function useDeleteBook() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: libraryApi.deleteBook,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['books', 'list'] })
    },
  })
}